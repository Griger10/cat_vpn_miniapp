import axios from "axios";
import {initData} from "@telegram-apps/sdk";

const base_url = import.meta.env.VITE_BASE_API_URL;

export const request = async (endpoint: string, method: string = "GET", data?: any) => {
    return await axios.request({
            method: method,
            url: `${base_url}/${endpoint}`,
            headers: {
              initData: `${initData.raw()}`,
              Accept: "application/json",
              "Content-Type": "application/json",
            },
            data: data ? JSON.stringify(data) : undefined,
        }
    );
}
