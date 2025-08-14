import axios from "axios";
import { initData } from "@telegram-apps/sdk";

let base_url = import.meta.env.VITE_BASE_API_URL;

export const request = async (endpoint, method = "GET", data = undefined) => {
    const response = await axios.request({
        method: method,
        url: `${base_url}/${endpoint}`,
        headers: {
            initData: `${initData.raw()}`,
            Accept: "application/json",
            "Content-Type": "application/json",
        },
        data: data? JSON.stringify(data) : undefined,
        }
    )

    return response;
}