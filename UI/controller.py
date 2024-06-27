import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_grafo(self, e):
        squadra = self._view.dd_squadra.value
        if squadra is None:
            self._view.create_alert("Selezionare una squadra")
            return
        grafo = self._model.creaGrafo(squadra)
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumNodes()} nodi."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumEdges()} archi."))
        for anno in grafo.nodes:
            self._view.dd_anno.options.append(ft.dropdown.Option(
                text=anno))
        self._view.update_page()


    def handle_dettagli(self, e):
            anno=self._view.dd_anno.value
            if anno is None:
                self._view.create_alert("Selezionare un anno")
                return
            dizionario=self._model.analisi(int(anno))
            for (nodo,peso) in dizionario:
                self._view.txt_result.controls.append(ft.Text(f"{anno}<->anno:{nodo}; peso:{peso}"))
            self._view.update_page()


    def fillDD(self):
        squadre=self._model.squadre
        for squadra in squadre:
            self._view.dd_squadra.options.append(ft.dropdown.Option(
                text=squadra))
