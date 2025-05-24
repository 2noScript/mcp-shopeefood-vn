

class ResourcesHint:
    CITIES = "Fetch supported cities on ShopeeFood."
    DISTRICTS = "Retrieve districts based on cities."

class ToolsHint:
    SEARCH_FOOD_SHOP = """
    Search for restaurants/food shops on ShopeeFood with filters.
    Tìm kiếm nhà hàng/quán ăn trên ShopeeFood với các bộ lọc.
    Args:
        location (str): City/province name to search in.
            Tên thành phố/tỉnh cần tìm kiếm.
            Example/Ví dụ: "Hà Nội", "TP. HCM"
        
        districts (List[str]): List of district names to filter results.
            Danh sách quận/huyện để lọc kết quả.
            Default/Mặc định: []
            Example/Ví dụ: ["Hoàn Kiếm", "Ba Đình"]
        
        keyword (str): Search keyword for restaurant/food name.
            Từ khóa tìm kiếm tên nhà hàng/món ăn.
            Default/Mặc định: ""
            Example/Ví dụ: "bún chả", "phở"
        
        limit (int): Maximum number of results to return.
                Số lượng kết quả tối đa trả về.
                Default/Mặc định: 25

    Returns:
        str: Formatted table of search results including:
             Bảng kết quả tìm kiếm được định dạng bao gồm:
             - name/Tên nhà hàng
             - address:/Địa chỉ
             - rating:/Đánh giá
             - review:/Số lượng đánh giá
             - open_time:/Giờ mở cửa
             - close_time:/Giờ đóng cửa
             - open/Trạng thái đóng cửa hay mở cửa 

    Note:
        All input strings are automatically URL decoded to support Vietnamese characters.
        Tất cả chuỗi đầu vào được tự động URL decode để hỗ trợ tiếng Việt có dấu.
    """


class PromptHint:
    pass
