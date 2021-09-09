{
    cellClass: (params: CellClassParams) => AgGridUtils.isEditable(params) ? "ag-cell-editable" : "",
    ...columnState && columnState['description']
}

{
    cellEditorParams: (params: ICellEditorParams): ICustomCellEditorParams => {
        params.data["value"] = params.data.value;
        return AgGridUtils.getNumberEditorParams('value',true)
    },
    ...columnState && columnState['parameterValue']
}