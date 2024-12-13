import { defineStore } from "pinia";
import { ref } from "vue";

export const useModalStore = defineStore("modal", () => {
  const isOpen = ref(false);
  const content = ref(null);
  const selectedTypeId = ref(null);
  const selectedTransaction = ref(null);
  const test = ref("test");

  const handleShowModal = () => {
    isOpen.value = !isOpen.value;
  };

  const changeModalContent = (newContent) => {
    content.value = newContent;
  };

  const setSelectedTypeId = (typeId) => {
    selectedTypeId.value = typeId;
  };

  const setSelectedTransaction = (transaction) => {
    selectedTransaction.value = transaction;
  };

  return {
    isOpen,
    content,
    selectedTypeId,
    selectedTransaction,
    handleShowModal,
    changeModalContent,
    setSelectedTypeId,
    setSelectedTransaction,
    test,
  };
});
