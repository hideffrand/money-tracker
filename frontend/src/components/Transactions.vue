<script>
import { onMounted } from "vue";
import { useTransactionStore } from "../stores/transaction";

export default {
  name: "Transactions",
  data() {
    storeTransaction: {
    }
  },
  methods: {
    fetchPost() {
      this.storeTransaction.fetchData();
    },
  },
  created() {
    this.storeTransaction = useTransactionStore();
    this.fetchPost();
  },
};
</script>

<template>
  <div v-if="this.storeTransaction.data">
    <h1>Transaction List</h1>
    <ul>
      <li v-for="item in storeTransaction.data" class="bg-red-400">
        <pre>{{ item.userId }} {{ item.id }}</pre>
        <pre>{{ item.title }}</pre>
      </li>
    </ul>
  </div>
  <div v-else>
    <p>Loading...</p>
  </div>
</template>
