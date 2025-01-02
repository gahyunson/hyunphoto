import { HandsontableBase } from './custom_change_list.js';


class PhotoHandsontable extends HandsontableBase {
    constructor() {
        super();
        this.requiredCol = ['photo_path','title'];
        this.initialize();
    }

    headerDict(header) {
        return header.map(h => ({
            data: h,
            readOnly: h === 'id' ? true: false,
        }));
    }

    // requiredColColor(col, TH) {
    //     const colName = this.tableData.header[col];
    //     if (this.requiredCol.includes(colName)) {
    //         TH.style.backgroundColor = '#417690'; // 강조 색상
    //         TH.style.color = '#FFFFFF'; // 텍스트 색상
    //     }
    // }
}

class PriceHandsontable extends HandsontableBase {
    constructor() {
        super();
        this.requiredCol = ['photo','size', 'price'];
        this.initialize();
    }

    headerDict(header) {
        return header.map(h => ({
            data: h,
            readOnly: h === 'id' ? true: false,
        }));
    }

    requiredColColor(col, TH) {
        const colName = this.tableData.header[col];
        if (this.requiredCol.includes(colName)) {
            TH.style.backgroundColor = '#417690'; // 강조 색상
            TH.style.color = '#FFFFFF'; // 텍스트 색상
        }
    }
}


const modelName = window.MODEL_NAME;
if (modelName === 'photo') {
    const hot = new PhotoHandsontable();
} else if (modelName === 'price') {
    const hot = new PriceHandsontable();
}


