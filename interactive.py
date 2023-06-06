from reactpy import component, html, run, hooks

@component
def ScreenshotComparison():
    file1 = "file2.jpg"
    file2 = "file2.jpg"
    pass_fail, set_pass_fail = hooks.use_state(None)

    def handle_pass():
        set_pass_fail("Pass")

    def handle_fail():
        set_pass_fail("Fail")

    return html.div(
        html.div(
            html.img(src=file1,),
            html.img(src=file2),
            style={"display": "flex"}
        ),
        html.div(
            html.button({"onClick": handle_pass}, "Pass"),
            html.button({"onClick": handle_fail}, "Fail"),
            style={"marginTop": "10px"}
        ),
        html.p("Status: ", pass_fail) if pass_fail else None
    )

run(ScreenshotComparison, port=8888)
