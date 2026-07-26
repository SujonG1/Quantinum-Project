from app import app

def test_app(dash_duo):
    
    dash_duo.start_server(app)
    
    dash_duo.wait_for_element("H1", "Pink Morsel Sales Dashboard", timeout=10)
    dash_duo.wait_for_element("#region-filter", timeout=10)
    dash_duo.wait_for_element("#interactive-line-chart", timeout=10)