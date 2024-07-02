import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { addUser } from "../store/services/formSlice";

const Form = () => {
  const dispatch = useDispatch()
  const [form, setForm] = useState({ name: "", email: "" });
  const [isFormEmpty, setIsFormEmpty] = useState('')

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(form);

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(form.email)) {
      setIsFormEmpty('Email Is Not Valid')
      return;
    }

    if(form.name === '' || form.email === ''){
      setIsFormEmpty('Please Fill All The Fields')
    }

    dispatch(addUser(form))
    return;
  
    
  };

  return (
    <>
      <div>
        <form
          onSubmit={handleSubmit}
          style={{
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            justifyContent: "center",
          }}
        >
          <label htmlFor="name">Name:</label>
          <input
            type="text"
            id="name"
            name="name"
            placeholder="Enter Name"
            value={form.name}
            onChange={handleChange}
          />

          <label htmlFor="email">Email:</label>
          <input
            type="email"
            id="email"
            name="email"
            placeholder="Enter email"
            value={form.email}
            onChange={handleChange}
          />

          <button type="submit">Send</button>
        </form>
      </div>
    </>
  );
};

export default Form;
