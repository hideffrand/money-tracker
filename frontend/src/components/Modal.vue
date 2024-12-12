<template>
  <div
    v-if="isOpen && content === 'AddNewTypeModal'"
    class="w-full h-screen flex items-center justify-center absolute z-10 backdrop-blur-sm"
  >
    <button @click="handleShowModal">Close</button>
    <AddNewTypeModal />
  </div>
</template>

<script>
import { useModalStore } from "../stores/modal";
import AddNewTypeModal from "./AddNewTypeModal.vue";

export default {
  components: {
    AddNewTypeModal,
  },
  setup() {
    const modalStore = useModalStore();

    return {
      isOpen: modalStore.isOpen,
      content: modalStore.content,
      handleShowModal: modalStore.handleShowModal,
    };
  },
};
</script>

<style scoped>
/* Add any styles for modal */
</style>
