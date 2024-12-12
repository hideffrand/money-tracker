<template>
  <div>
    <h2>Add New Type</h2>
    <form @submit.prevent="handleSubmit">
      <input v-model="description" type="text" placeholder="Description" />
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
import { ref } from "vue";
import { useModalStore } from "../stores/modal";
import { API_BASE_URL } from "../config";

export default {
  setup() {
    const modalStore = useModalStore();
    const description = ref("");

    const handleSubmit = async () => {
      const res = await fetch(`${API_BASE_URL}/types`, {
        method: "POST",
        body: JSON.stringify({ description: description.value }),
        headers: {
          "Content-Type": "application/json",
        },
      });

      if (res.ok) {
        // Close the modal after successful submission
        modalStore.handleShowModal();
      }

      // Handle response as needed
    };

    return {
      description,
      handleSubmit,
    };
  },
};
</script>

<style scoped>
/* Add any styles for the AddNewTypeModal form */
</style>
