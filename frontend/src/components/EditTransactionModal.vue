<template>
  <div class="space-y-4">
    <h2 class="text-2xl font-semibold text-center text-gray-700">
      Edit Transaction {{ selectedTransaction.title }}
      <br />
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
        type="text"
        class="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        v-model="selectedTypeName"
        readonly
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
      <div class="flex gap-2">
        <button
          type="button"
          class="w-full py-3 bg-red-600 text-white font-semibold rounded-md hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-500"
          @click="deleteTransaction"
        >
          Delete
        </button>
        <button
          type="submit"
          class="w-full py-3 bg-blue-600 text-white font-semibold rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
        >
          Save
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import { useModalStore } from "../stores/modal";
import { ref, onMounted, computed, watchEffect } from "vue";
import { useRouter } from "vue-router";
import { API_BASE_URL } from "../config";

export default {
  setup() {
    const userId = ref(null);
    const title = ref("");
    const description = ref("");
    const amount = ref("");
    const router = useRouter();
    const modalStore = useModalStore();
    const transactionId = ref();
    const selectedTypeName = ref("");

    // Get the selected transaction from the modal store
    const selectedTransaction = computed(() => modalStore.selectedTransaction);

    // Initialize the form fields with the selected transaction's data
    onMounted(() => {
      if (selectedTransaction.value) {
        title.value = selectedTransaction.value.title || "";
        description.value = selectedTransaction.value.description || "";
        amount.value = selectedTransaction.value.amount || "";
        transactionId.value = selectedTransaction.value.transaction_id || "";
      }

      const cookies = document.cookie.split(";").reduce((acc, cookie) => {
        const [name, value] = cookie.trim().split("=");
        acc[name] = value;
        return acc;
      }, {});

      const token = cookies.token;
      const userIdFromCookie = cookies.userId;

      if (!token || !userIdFromCookie) {
        router.push("/login");
      } else {
        userId.value = parseInt(userIdFromCookie);
      }
    });

    // Handle form submission
    const handleSubmit = async () => {
      console.log(selectedTransaction.value);
      const res = await fetch(`${API_BASE_URL}/transactions/update`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          transaction_id: selectedTransaction.value.transaction_id,
          type_id: selectedTransaction.value.type_id,
          description: description.value,
          title: title.value,
          amount: amount.value,
          user_id: userId.value,
        }),
      });

      if (!res.ok) {
        alert("Failed to update transaction");
        return;
      }

      alert("Transaction updated successfully!");
      //   modalStore.isOpen = false;
      //   router.push("/");
      window.location.reload();
    };

    const getTypeName = async () => {
      try {
        const res = await fetch(
          `http://localhost:5000/api/types/get_type/${selectedTransaction.value.type_id}`
        );
        if (!res.ok) throw new Error("Failed to fetch type name");

        const data = await res.json();
        selectedTypeName.value = data.data;
      } catch (error) {
        alert(error.message);
      }
    };

    const deleteTransaction = async () => {
      try {
        const res = await fetch(
          `http://localhost:5000/api/transactions/${selectedTransaction.value.transaction_id}`,
          { method: "DELETE" }
        );
        if (!res.ok) throw new Error("Failed to delete transaction");

        window.location.reload();
      } catch (error) {
        alert(error.message);
      }
    };

    // Use watchEffect to reactively watch selectedTransaction
    watchEffect(() => {
      if (selectedTransaction.value) {
        getTypeName();
      }
    });

    return {
      userId,
      title,
      description,
      amount,
      transactionId,
      selectedTransaction,
      handleSubmit,
      selectedTypeName,
      deleteTransaction,
    };
  },
};
</script>

<style scoped>
/* Add your custom styles if necessary */
</style>
