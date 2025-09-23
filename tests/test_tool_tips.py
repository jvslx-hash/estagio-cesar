from pages.tool_tips_page import Tooltipspage
import time


def test_tool_tips(driver):
    tool_tips = Tooltipspage(driver)
    tool_tips.navigate()

    tool_tips.move_to_button()
    time.sleep(2)       
    assert tool_tips.tooltip.is_displayed()
    assert tool_tips.tooltip.button == "You hovered over the Button"

    tool_tips.move_to_text()
    time.sleep(2)
    assert tool_tips.tooltip.is_displayed()
    assert tool_tips.tooltip.text == "You hovered over the text field"

