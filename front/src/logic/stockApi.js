import axios from 'axios';

const DEFAULT_STOCK_URL = "https://private-406ee0-stock33.apiary-mock.com/stock";

export default class StockApi {

    
    static list() {
        return axios.get(DEFAULT_STOCK_URL);
    }

    static listAlert() {
        return axios.get(`${DEFAULT_STOCK_URL}/alerts`);
    }

    static createAlert(id, price, action) {
        return axios.post(`${DEFAULT_STOCK_URL}/alerts`, {id, price, user_id: 1, action});
    }
}