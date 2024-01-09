from robocorp.tasks import task
from robocorp.browser import browser, BrowserContext, Page
import os

def open_page(ctx: BrowserContext, url: str) -> Page:
  page = ctx.new_page()
  page.goto(url)
  return page

@task
def interact_with_input_fields() -> None:
  ctx = browser().new_context()

  try:
    page: Page = open_page(ctx, "https://lwc-recipes-oss.herokuapp.com")
    page.locator("recipe-hello-expressions ui-input:nth-child(1) input").type("First name")
    page.locator("recipe-hello-expressions ui-input:nth-child(2) input").type("Last name")
    localor = page.locator("css=recipe-hello-expressions ui-card .card-body")
    localor.screenshot(type="png", path=f"{os.path.join(os.environ['ROBOT_ARTIFACTS'], 'input_fields.png')}")
  finally:
    ctx.close()

@task
def interact_with_dynamic_fields() -> None:
  ctx = browser().new_context()

  try:
    page: Page = open_page(ctx, "https://lwc-recipes-oss.herokuapp.com/#composition")
    page.locator("recipe-composition-contact-search input[type='search']").type("Amy")
    locator = page.locator("recipe-composition-contact-search recipe-contact-tile")
    locator.wait_for()
    locator.screenshot(type="png", path=f"{os.path.join(os.environ['ROBOT_ARTIFACTS'], 'dynamic_fields.png')}")
  finally:
    ctx.close()