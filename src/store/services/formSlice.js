import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";

const initialState= {
    users: []
}

export const fetchUsers = createAsyncThunk(
    "form/fetchUsers",
    async (args, { rejectWithValue }) => {
        try {
            const response = await fetch('https://6682f9f34102471fa4c8d8e0.mockapi.io/user')
            const data = await response.json()
            return data;
        } catch (error) {
            rejectWithValue(error.message)
        }
    }
)


export const formSlice= createSlice({
    name: 'form',
    initialState,
    reducers:{
        addUser: (state, action) => {
            state.users.push(action.payload)
        }
    },

    extraReducers: (builder) => {
        builder.addCase(fetchUsers.fulfilled, (state, action) => {
            state.users = action.payload
        })
    
    }
})

export const { addUser } = formSlice.actions

export default formSlice.reducer