export class HandsontableBase {
    constructor() {
        this.container = document.querySelector('#spreadsheet');
        this.tableData = JSON.parse(document.getElementById('table-data').textContent);
        this.loadButton = document.querySelector('#load');
        this.saveButton = document.querySelector('#save');

        this.requiredCol = [];

        this.genTempIds = new Set();
        this.tempNewIds = [];
        this.sortConfig = [];
        this.changedRows = [];
        this.deletedRows = [];

        this.hot = null;
        this.initialize();
        this.addEventListener();
    }

    headerDict(header) {
        return header.map(h => ({
            data: h,
            readOnly: h === 'id' ? true: false
        }));
    }

    getNestedHeaders() {
        // console.log(this.tableData.header);
        return [this.tableData.header];
    }

    handleAfterCreateRow(index, amount) {
        for (let i = 0; i < amount; i++) {
            var tempId = this.generateTempId();
            this.hot.setDataAtCell(index+i, 0, tempId);
        }
    }

    handleAfterChange(changes, source) {
        if (!changes) return;

        changes.forEach(change => {
            const rowId = this.hot.getDataAtCell(change[0], 'id')
            if (rowId > 0) {
                change[0] = rowId;
                this.changedRows.push(change);
            } else {
                this.tempNewIds.push(rowId);
            }
        });
    }

    handleBeforeRemoveRow(index, amount) {
        for (let i = index; i < index+amount; i++){
            const removedDataId = this.hot.getDataAtCell(i, 'id');
            if (removedDataId > 0) {
                this.deletedRows.push(removedDataId);
            }
        }
    }

    generateTempId() {
        let tempId;
        do {
            tempId = -1*(Math.floor(Math.random()*900)+10)
        } while (this.genTempIds.has(tempId));

        this.genTempIds.add(tempId);
        return tempId;
    }

    getRowData(tempNewIds) {
        this.tempNewIds = Array.from(this.tempNewIds);
        const wholeData = this.hot.getData();
        return wholeData.filter(data => this.tempNewIds.includes(data[0]));
    }

    initialize() {
        this.hot = new Handsontable(this.container, {
            licenseKey: 'non-commercial-and-evaluation',
            data: this.tableData.body,
            columns: this.headerDict(this.tableData.header),
            colHeaders: true,
            rowHeaders: true,
            nestedHeaders: this.getNestedHeaders(),
            collapsibleColumns: true,
            fixedColumnsStart: 1,
            width: '100%',
            height: '50rem',

            dropdownMenu: true,
            multiColumnSorting: true,
            beforeColumnSort: (currentSortConfig, destinationSortConfigs) => {
                this.sortConfig = destinationSortConfigs;
            },
            afterColumnSort: (currentSortConfig, destinationSortConfigs) => {
                this.sortConfig = destinationSortConfigs
            },
            filters: true,
            manualColumnResize: true,
            autoWrapCol: true,
            autoWrapRow: true,
            autoColumnSize: {useHeaders: true},
            autoRowSize: true,
            wordWrap: false,
            colWidths: 300,
            persistentState: true,

            contextMenu: true,
            afterCreateRow: (index, amount) => this.handleAfterCreateRow(index, amount),
            afterChange: (changes, source) => this.handleAfterChange(changes, source),
            beforeRemoveRow: (index, amount) => this.handleBeforeRemoveRow(index, amount),

            afterGetColHeader: (col, TH) => this.requiredColColor(col, TH),

        });
    }

    requiredColColor(col, TH) {
        const colName = this.tableData.header[col];
        if (this.requiredCol.includes(colName)) {
            TH.style.backgroundColor = '#417690'; // 강조 색상
            TH.style.color = '#FFFFFF'; // 텍스트 색상
        }
    }

    addEventListener() {
        this.loadButton.addEventListener('click', e => this.handleLoad(e));
        this.saveButton.addEventListener('click', e => this.handleSave(e));
    }

    resetState() {
        this.changedRows = [];
        this.deletedRows = [];
        this.tempNewIds = [];
        this.genTempIds.clear();
    }

    handleLoad(event) {
        event.preventDefault();

        fetch(window.location.href, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': document.querySelector('input[name="csrfmiddlewaretoken"]').value
            },
            body: JSON.stringify({ action: 'load' }),
        })
        .then(response => {
            if (!response.ok) {
                return response.json().then(error => {
                    throw new Error(error.message);
                });
            }
            return response.json();
        })
        .then(data => {
            this.resetState();
            this.hot.updateData(data.data);
            this.hot.getPlugin('multiColumnSorting').sort(this.sortConfig);
        })
        .catch(error => {
            alert(error.message);
        })
    }

    handleSave(event) {
        event.preventDefault();
        console.log(this.getRowData(this.genTempIds));

        fetch(window.location.href, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': document.querySelector('input[name="csrfmiddlewaretoken"]').value
            },
            body: JSON.stringify({
                action: 'save',
                insertedData: this.getRowData(this.genTempIds),
                changedData: this.changedRows,
                deletedData: this.deletedRows,
            }),
        })
        .then(response => {
            if (!response.ok) {
                return response.json().then(error => {
                    throw new Error(error.message);
                });
            }
            return response.json();
        })
        .then(data => {
            console.log(data.message);
            this.resetState();
            this.hot.updateData(data.data);
            this.hot.getPlugin('multiColumnSorting').sort(this.sortConfig);
            alert(data.message);
        })
        .catch(error => {
            console.log(error);
            window.location.reload();
            alert(error.message);
        })
    }
}
