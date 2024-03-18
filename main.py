import flet


class App:
    def __init__(self, width: int = None, height: int = None):
        self.width = width
        self.height = height
        self.page = None

    def main(self, page: flet.Page):
        self.page = page
        if self.page.platform != 'android':
            self.page.window_max_width = self.width
            self.page.window_max_height = self.height
        self.page.update()
        self._build_home()

    def _build_home(self):
        self.browser = Browser()

        self.page.add(flet.SafeArea(content=self.browser))


class Browser(flet.UserControl):
    def __init__(self, *w, **kw):
        super(Browser, self).__init__(*w, **kw)
        self.url = None
        self.webview = None

    def build(self):
        self.url = flet.TextField(value='about:blank')
        self.webview = flet.WebView('about:blank', javascript_enabled=True)
        return flet.Column(controls=[
                self.url,
                self.webview,
            ], expand=True, alignment=flet.MainAxisAlignment.CENTER)


if __name__ == '__main__':
    app = App()
    flet.app(target=app.main, name='flikfront')
