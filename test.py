a = ["a","b",[None,5]]

a[2] = ["",5]

print(a)


import flet as ft



def main(page: ft.Page):

    def open_url(e):
        page.launch_url(e.data)

    c = ft.Tab(content=ft.Text("lol"))
    c.content.value = "mo"

    t = ft.Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[
            c
        ],
        expand=1,
    )


    page.add(
        ft.Markdown(
            "[inline-style](https://www.google.com)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=True,
        ),
        t
    )

ft.app(target=main)

