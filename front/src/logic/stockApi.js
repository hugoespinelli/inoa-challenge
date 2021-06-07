import axios from 'axios';

const DEFAULT_STOCK_URL = "http://localhost:5000/stock";

export default class StockApi {

    
    static list() {
        return axios.get(DEFAULT_STOCK_URL);
    }

    static listAlert() {
        return axios.get(`${DEFAULT_STOCK_URL}/alert`);
    }

    static createAlert(id, price, action) {
        return axios.post(
            `${DEFAULT_STOCK_URL}/alert`, 
            {id_stock: id, price_alert: price, id_user: 1, type: action.toLowerCase()}
        );
    }
}