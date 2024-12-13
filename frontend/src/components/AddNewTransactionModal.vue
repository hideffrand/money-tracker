<template>
  <div class="space-y-4">
    <h2 class="text-2xl font-semibold text-center text-gray-700">
      Add New {{ selectedTypeName }} Transaction
    </h2>
    <form @submit.prevent="handleSubmit" class="space-y-4">
      <input
        v-model="userId"
        type="text"
        placeholder="User ID"
        class="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        required
        hidden
      />
      <input
        v-model="title"
        type="text"
        placeholder="Title"
        class="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        required
      />
      <input
        v-model="description"
        type="text"
        placeholder="Description"
        class="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        required
      />
      <input
        v-model="amount"
        type="number"
        placeholder="Amount"
        class="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        required
      />
      <button
        type="submit"
        class="w-full py-3 bg-blue-600 text-white font-semibold rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
      >
        Add Transaction
      </button>
    </form>
  </div>
</template>

<script>
import { ref, onMounted, computed, watchEffect } from "vue";
import { useRouter } from "vue-router";
import { API_BASE_URL } from "../config";
import { useModalStore } from "@/stores/modal";

export default {
  setup() {
    const userId = ref(null);
    const title = ref("");
    const description = ref("");
    const amount = ref("");
    const router = useRouter();
    const modalStore = useModalStore();
    const selectedTypeName = ref("");

    const handleSubmit = async (e) => {
      const res = await fetch(`${API_BASE_URL}/transactions/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          type_id: modalStore.selectedTypeId,
          user_id: userId.value,
          title: title.value,
          description: description.value,
          amount: amount.value,
        }),
      });

      if (!res.ok) {
        alert("Failed to add new transaction");
      } else {
        alert("Transaction added successfully!");
        window.location.reload();
      }
    };

    onMounted(() => {
      const cookies = document.cookie.split(";").reduce((acc, cookie) => {
        const [name, value] = cookie.trim().split("=");
        acc[name] = value;
        return acc;
      }, {});

      const token = cookies.token;
      const userIdCookie = cookies.userId;

      if (!token || !userIdCookie) {
        router.push("/login");
      } else {
        userId.value = parseInt(userIdCookie);
      }
    });

    const getTypeName = async () => {
      try {
        const res = await fetch(
          `${API_BASE_URL}/types/get_type/${modalStore.selectedTypeId}`
        );
        if (!res.ok) throw new Error("Failed to fetch type name");

        const data = await res.json();
        selectedTypeName.value = data.data;
      } catch (error) {
        alert(error.message);
      }
    };

    // Watch the modalStore.selectedTypeId to reactively update the type name
    watchEffect(() => {
      if (modalStore.selectedTypeId) {
        getTypeName();
      }
    });

    return {
      userId,
      title,
      description,
      amount,
      handleSubmit,
      modalStore,
      selectedTypeName,
    };
  },
};
</script>

<style scoped>
/* Add your custom styles if necessary */
</style>
