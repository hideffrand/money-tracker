<template>
  <Transactions />
</template>

<script>
import { ref, onMounted, watch } from "vue";
import { useRouter } from "vue-router";
import { API_BASE_URL } from "../config";
import Transactions from "@/components/Transactions.vue";

export default {
  name: "HomeView2",
  components: {
    Transactions,
  },
};
</script>

<style scoped>
/* Add your styles here */
</style>
