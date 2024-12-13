<template>
  <div
    v-if="modalStore.isOpen"
    class="fixed top-0 left-0 w-full h-full bg-black bg-opacity-50 flex items-center justify-center z-50"
  >
    <div
      class="bg-white p-8 rounded-lg shadow-xl relative w-full max-w-lg animate__animated animate__fadeIn animate__faster"
    >
      <button
        @click="handleCloseModal"
        class="absolute top-4 right-4 text-2xl font-bold text-gray-500 hover:text-gray-700"
      >
        &times;
      </button>
      <AddNewTypeModal v-if="modalStore.content === 'AddNewTypeModal'" />
      <AddNewTransactionModal
        v-if="modalStore.content === 'AddNewTransactionModal'"
      />
      <EditTransactionModal
        v-if="modalStore.content === 'EditTransactionModal'"
      />
    </div>
  </div>
</template>

<script>
import { useModalStore } from "../stores/modal";
import AddNewTypeModal from "./AddNewTypeModal.vue";
import AddNewTransactionModal from "./AddNewTransactionModal.vue";
import EditTransactionModal from "./EditTransactionModal.vue";

export default {
  components: {
    AddNewTypeModal,
    AddNewTransactionModal,
    EditTransactionModal,
  },
  setup() {
    const modalStore = useModalStore();

    function handleCloseModal() {
      modalStore.isOpen = false;
    }

    return {
      modalStore,
      handleCloseModal,
    };
  },
};
</script>
