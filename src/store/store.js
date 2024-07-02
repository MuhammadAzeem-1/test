import { configureStore } from "@reduxjs/toolkit";
import formSlice from "./services/formSlice";

export const store = configureStore({
    reducer:{
        users: formSlice
    }
})