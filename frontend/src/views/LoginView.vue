<template>
  <div class="flex justify-center items-center min-h-screen bg-gray-100">
    <div class="bg-white p-8 rounded-lg shadow-lg w-full max-w-sm">
      <h2 class="text-2xl font-bold text-center text-gray-700 mb-6">Login</h2>
      <form @submit.prevent="handleLogin" class="space-y-4">
        <input
          v-model="email"
          type="email"
          placeholder="Email"
          class="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400"
        />
        <input
          v-model="password"
          type="password"
          placeholder="Password"
          class="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400"
        />
        <button
          type="submit"
          class="w-full py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition duration-200"
        >
          Login
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { API_BASE_URL } from '../config'; // Make sure to adjust the path if needed

export default {
  name: 'LoginView',
  setup() {
    const router = useRouter();
    const email = ref('');
    const password = ref('');

    const handleLogin = async () => {
      if (!email.value || !password.value) {
        alert("Please fill in both fields");
        return;
      }

      try {
        const res = await fetch(`${API_BASE_URL}/auth/login`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            email: email.value,
            password: password.value,
          }),
        });

        if (!res.ok) {
          alert('Failed to Login');
          return;
        }

        const parsed = await res.json();
        const token = parsed.data.token;
        document.cookie = `token=${token}; path=/; max-age=3600`;

        const userId = parsed.data.user.user_id;
        document.cookie = `userId=${userId}; path=/; max-age=3600`;

        alert('Login Success!');
        router.push('/'); // Navigate to the home page
      } catch (error) {
        console.error('Login error:', error);
        alert('An error occurred during login.');
      }
    };

    return {
      email,
      password,
      handleLogin,
    };
  },
};
</script>

<style scoped>
/* Add your custom styles here */
</style>
