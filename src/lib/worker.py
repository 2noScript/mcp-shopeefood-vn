from camoufox.async_api import AsyncCamoufox
from browserforge.fingerprints import Screen
from typing import Any, Callable, List
import asyncio

_constrains = Screen(max_width=1280, max_height=720)
_browser = None
_active_tasks = 0
_cleanup_task = None

async def _cleanup_browser():
    """
    Check and close browser if no active tasks.
    """
    global _browser, _active_tasks
    while True:
        await asyncio.sleep(900)  # Check every 15 minutes
        if _browser and _active_tasks == 0:
            await _browser.close()
            _browser = None
            print("Browser closed due to inactivity")
            break

async def run_task(handle: Callable, args: List[Any]):
    """
    Run a task with a browser shared between calls.
    
    Args:
        handle: Task handler function
        args: List of parameters for the handler
    
    Returns:
        Result from the handler function
    
    Raises:
        Exception: When an error occurs during processing
    """
    global _browser, _active_tasks, _cleanup_task
    try:
        _active_tasks += 1
        if _browser is None:
            _browser = await AsyncCamoufox(
                i_know_what_im_doing=True,
                screen=_constrains,
                os=('windows', 'macos', 'linux'),
                block_images=True,
                humanize=True,
                # headless=True,
                block_webrtc=True,
                config={
                    'disableTheming': True
                }
                
            ).start()
            _cleanup_task = asyncio.create_task(_cleanup_browser())
        
        page = await _browser.new_page()
        try:
            result = await handle(page, *args)
            print(f"Task completed: {result}")
            return result
        finally:
            await page.close()
    except Exception as e:
        print(f"Error during task processing: {str(e)}")
        raise
    finally:
        _active_tasks -= 1
