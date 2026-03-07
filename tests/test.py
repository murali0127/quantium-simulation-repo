import pytest
from dashboard import app

def header_test(dash_duo):
      dash_duo.start_server(app)
      header = dash_duo.find_element('#header')
      assert header is not None

def visualizer_text(dash_duo):
      dash_duo.start_server(app)
      graph = dash_duo.find_element('#total-sales')
      assert graph is not None



def test_region_filter(dash_duo):
      dash_duo.start_server(app)
      region_picker = dash_duo.find_element('#region-filter')
      assert region_picker is not None