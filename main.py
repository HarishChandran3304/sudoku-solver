from flet import *
from helpers import *
from copy import deepcopy

OG = [[0]*9]*9
GRID = [[0]*9]*9


def main(page: Page):

    # Helpers
    def get_path_result(e: FilePickerResultEvent):
        if e.path:
            try:
                global OG, GRID
                filename = e.path
                GRID = getgrid(filename)
                OG = deepcopy(GRID)
                _sudoku_container.content = get_sudoku_container(GRID)
                solve_btn.content = solve_btn.content = Text(value="SOLVE", size=50, color="white")
                solve_btn.disabled = False
                page.update()

            except:
                page.dialog = invalid_dlg
                invalid_dlg.open = True
                page.update()
    
    def solve_clicked(e):
        solve_btn.content = Text(value="SOLVING...", size=50, color="white")
        solve_btn.disabled = True
        import_btn.disabled = True
        page.update()
        found = visualize(page, _sudoku_container, GRID)

        if found: 
            solve_btn.content = Text(value="SOLVED!", size=50, color="white")
            import_btn.disabled = False
            page.update()
        else:
            page.dialog = impossible_dlg
            impossible_dlg.open = True
            _sudoku_container.content = get_sudoku_container(OG)
            solve_btn.disabled = False
            solve_btn.content = Text(value="SOLVE", size=50, color="white", text_align=TextAlign.CENTER)
            import_btn.disabled = False
            page.update()
    
    def close_impossible_dlg(e):
        impossible_dlg.open = False
        page.update()
    
    def close_invalid_dlg(e):
        invalid_dlg.open = False
        page.update()
    

    # Page Setup   
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.title = "Sudoku Solver"


    # Dialogs
    impossible_dlg = AlertDialog(
        title=Text("No possible solution"),
        modal=True,
        actions=[TextButton("Dismiss", on_click=close_impossible_dlg)],
        actions_alignment=MainAxisAlignment.END
    )
    invalid_dlg = AlertDialog(
        title=Text("Invalid file/format"),
        modal=True,
        actions=[TextButton("Dismiss", on_click=close_invalid_dlg)],
        actions_alignment=MainAxisAlignment.END
    )


    # Main Container
    _main = Container(
        width=600,
        height=page.height*0.975,
        bgcolor="black",
        padding=8,
        border_radius=35,
        alignment=alignment.center
    )


    # Main Column
    _main_column = Column(spacing=2, alignment=MainAxisAlignment.SPACE_EVENLY)


    # Sudoku Container
    _sudoku_container = Container(
        alignment=alignment.center
    )
    _sudoku_container.content = get_sudoku_container(GRID)


    # Buttons Container
    _btns_container = Container(
        height=100,
        alignment=alignment.center
    )
    _btns_row = Row(spacing=2, alignment=MainAxisAlignment.SPACE_EVENLY)
    solve_btn = ElevatedButton(
        disabled=True,
        bgcolor="green",
        content=Text(
            value="SOLVE",
            size=50,
            color="white"),
        on_click=solve_clicked)
    get_path = FilePicker(on_result=get_path_result)
    page.overlay.append(get_path)
    import_btn = ElevatedButton(
        bgcolor="green",
        content=Text(
            value="IMPORT",
            size=50,
            color="white"),
        on_click=lambda _: get_path.save_file(initial_directory=".", allowed_extensions=["txt"]))
    _btns_row.controls = [import_btn, solve_btn]
    _btns_container.content = _btns_row
    
    


    # Populating Page
    _main_column.controls.append(_sudoku_container)
    _main_column.controls.append(_btns_container)
    _main.content = _main_column
    page.add(_main)


if __name__ == "__main__":
    app(target=main)