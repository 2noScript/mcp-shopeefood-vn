from camoufox.async_api import AsyncCamoufox
from browserforge.fingerprints import Screen
from typing import Any, Callable, List

_constrains = Screen(max_width=1280, max_height=720)
_browser = None

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
    global _browser
    try:
        if _browser is None:
            _browser = await AsyncCamoufox(
                i_know_what_im_doing=True,
                screen=_constrains,  # Sửa lỗi tên biến
                os=('windows', 'macos', 'linux'),
                block_images=True,
                humanize=True,
                headless=True,
                block_webrtc=True
            )
        page = await _browser.new_page()
        try:
            result = await handle(page, *args)
            return result
        finally:
            await page.close()
    except Exception as e:
        print(f"Lỗi trong quá trình xử lý task: {str(e)}")
        raise
