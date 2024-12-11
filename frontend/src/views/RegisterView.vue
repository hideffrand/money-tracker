<template>
    <form @submit.prevent="login">
      <div class="mb-4">
        <h1 class="text-lg font-bold">Username</h1>
        <input
          type="text"
          v-model="name"
          class="w-full p-2 border border-gray-400"
          required
        />
        
      <div class="mb-4">
        <h1 class="text-lg font-bold">Email</h1>
        <input
          type="email"
          v-model="email"
          class="w-full p-2 border border-gray-400"
          required
        />
      </div>
  
      <div class="mb-4">
        <h1 class="text-lg font-bold">Password</h1>
        <input
          type="password"
          v-model="password"
          class="w-full p-2 border border-gray-400"
          required
        />
      </div>
      

      </div>
      <button class="blue-300" type="submit">Register</button>
    </form>
  </template>
  
  <script>
  export default {
    name: "RegisterView",
    data() {
      return {
        name: "",
        email: "",
        password: ""
      };
    },
    methods: {
      async login() {
        try {
          const response = await fetch("http://localhost:5000/api/auth/register", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              name: this.name,
              email: this.email,
              password: this.password,
            }),
          });
  
          if (response.ok) {
            alert("Registration Success");
            this.$router.push("/login");
          }
        } catch (error) {
          console.error(error);
        }
      },
    },
  };
  </script>
  