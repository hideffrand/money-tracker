<template>
  <div class = "flex justify-center items-center min-h-screen bg-gray-100">
    <div class="bg-white p-8 rounded-lg shadow-lg w-full max-w-sm">
      <h2 class="text-2xl font-bold text-center text-gray-700 mb-6">Register</h2>
      <form @submit.prevent="handleRegister">

      <div class="mb-4">
        <h1 class="text-lg font-bold">name</h1>
        <input type="text" v-model="name" class="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400" required />
      </div>
      
      <div class="mb-4">
        <h1 class="text-lg font-bold">Email</h1>
        <input type="email" v-model="email" class="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400" required />
      </div>
      
      <div class="mb-4">
        <h1 class="text-lg font-bold">Password</h1>
        <input type="password" v-model="password" class="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400" required />
      </div>
      
      <button class="bg-blue-300 text-white py-2 px-4 rounded" type="submit">Register</button>
    </form>
    </div>
  </div>
  </template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { API_BASE_URL } from '../config'; // Adjust the path as needed

export default {
  name: 'RegisterView',
  setup() {
    const router = useRouter();
    const name = ref('');
    const email = ref('');
    const password = ref('');

    const handleRegister = async () => {
      if (!email.value || !password.value || !name.value) {
        alert('Please fill in all fields');
        return;
      }

      try {
        const res = await fetch(`${API_BASE_URL}/auth/register`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            name: name.value,
            email: email.value,
            password: password.value,
          }),
        });

        if (!res.ok) {
          const errorData = await res.json();
          alert(`Failed to Register: ${errorData.message || 'Unknown error'}`);
          return;
        }

        alert('Register Success!');
        router.push('/login'); // Navigate to the login page
      } catch (error) {
        console.error('Register error:', error);
        alert('An error occurred during registration.');
      }
    };

    return {
      name, 
      email,
      password,
      handleRegister,
    };
  },
};
</script>
