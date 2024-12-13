<template>
  <div class="space-y-4">
    <h2 class="text-2xl font-semibold text-center text-gray-700">Add New Type</h2>
    <form @submit.prevent="handleSubmit" class="space-y-4">
      <input v-model="userId" type="hidden" />
      <input v-model="description" type="text" placeholder="Enter description" class="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500" required />
      <input v-model="budget" type="number" placeholder="Budget" class="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500" required />
      <button type="submit" class="w-full py-3 bg-blue-600 text-white font-semibold rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500">
        Add Type
      </button>
    </form>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { useModalStore } from '../stores/modal';

export default {
  setup() {
    const modalStore = useModalStore();
    const userId = ref(null);
    const description = ref('');
    const budget = ref('');

    const handleSubmit = async () => {
      const res = await fetch(`${API_BASE_URL}/types/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          user_id: userId.value,
          description: description.value,
          budget: budget.value,
        }),
      });

      if (!res.ok) {
        alert('Failed to add new type');
        return;
      }

      alert('Type added successfully!');
      window.location.reload();
    };

    onMounted(() => {
      const cookies = document.cookie.split(';').reduce((acc, cookie) => {
        const [name, value] = cookie.trim().split('=');
        acc[name] = value;
        return acc;
      }, {});

      const token = cookies.token;
      const userIdFromCookie = cookies.userId;

      if (!token || !userIdFromCookie) {
        // handle redirect to login
      } else {
        userId.value = parseInt(userIdFromCookie);
      }
    });

    return {
      userId,
      description,
      budget,
      handleSubmit,
    };
  },
};
</script>
