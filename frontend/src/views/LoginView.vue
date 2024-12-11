<template>
  <form @submit.prevent="login">
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
    <button class="blue-300" type="submit">Login</button>
  </form>
</template>

<script>
export default {
  name: "LoginView",
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    async login() {
      try {
        const response = await fetch("http://localhost:5000/api/auth/login", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            email: this.email,
            password: this.password,
          }),
        });

        if (response.ok) {
          alert("Login Success");
          this.$router.push("/");
        }
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>
