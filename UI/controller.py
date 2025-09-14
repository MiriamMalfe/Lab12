import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._listYear = []
        self._listCountry = []

    def fillDDCountry(self, dd: ft.Dropdown()):
        self._listCountry = self._model.listaNazione()
        for c in self._listCountry:
            dd.options.append(ft.dropdown.Option(text=c,
                                                 data=c,
                                                 on_click=self.readDDCountry))

    def readDDCountry(self, e):
        if e.control.data is None:
            self.country = None
        else:
            self.country = e.control.data


    def fillDDAnno(self, dd: ft.Dropdown()):
        self._listYear = self._model.listaAnni()
        for c in self._listYear:
            dd.options.append(ft.dropdown.Option(text=c,
                                                 data=c,
                                                 on_click=self.readDDAnno))

    def readDDAnno(self, e):
        if e.control.data is None:
            self.anno = None
        else:
            self.anno = e.control.data

    def handle_graph(self, e):
        self._model.creaGrafo(self.country, self.anno)

    def handle_volume(self, e):
        daStampare = self._model.volume()
        self._view.txtOut2.controls.clear()
        self._view.txtOut2.controls.append(ft.Text(daStampare))
        self._view.update_page()


    def handle_path(self, e):
        pass
