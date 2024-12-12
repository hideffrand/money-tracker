<template>
<div>
    <form @submit.prevent="handleAddTransaction" class="space-y-4">
        <input
          v-model="title"
          type="text"
          placeholder="Transaction Title"
          class="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400"
        />
        <input
          v-model="description"
          type="text"
          placeholder="Description"
          class="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400"
        />
        <input
          v-model="amount"
          type="number"
          placeholder="Amount Spent"
          class="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400"
        />
        <input
        v-model="type"
          type="text"
          placeholder="Type"z
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
</template>
<script>

import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { API_BASE_URL } from '../config'; // Make sure to adjust the path if needed
import {defineStore} from 'pinia'

export default {
  name: 'FormView',
  setup() {
    const router = useRouter();
    const title = ref('');
    const description = ref('');
    const amount = ref('');
    const type = ref('');

    const handleLogin = async () => {
      let user_id = getCookie("user_id");
      if (!user_id) {
        alert("User ID Not Found")
      }

      if (!router.value || !title.value || !description.value || !amount.value || !type_id.value ) {
        alert("Please fill in all fields");
        return;
      }

      try {
        const res = await fetch(`${API_BASE_URL}/transaction`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            user_id: user_id,
            title: title.value,
            description: password.value,
            amount: amount.value,
            type_id: type.value
          }),
        });

        if (!res.ok) {
          alert('Failed to Post Card');
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
