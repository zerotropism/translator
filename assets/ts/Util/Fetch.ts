import axios, {AxiosRequestConfig, AxiosResponse} from 'axios';

export default class Fetch {
    get<T = any, R = AxiosResponse<T>>(url: string, config?: AxiosRequestConfig): Promise<R> {
        return axios.get(url, config);
    }

    post<T = any, R = AxiosResponse<T>>(url: string, data?: any, config?: AxiosRequestConfig): Promise<R> {
        return axios.post(url, data, config);
    }

    put<T = any, R = AxiosResponse<T>>(url: string, data?: any, config?: AxiosRequestConfig): Promise<R> {
        return axios.put(url, data, config);
    }
}