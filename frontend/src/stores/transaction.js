// src/stores/transaction.js
import { defineStore } from "pinia";

const API_BASE_URL = "http://localhost:5000/api";

export const useTransactionStore = defineStore({
  id: "transaction",
  state: () => ({
    data: [],
  }),
  actions: {
    fetchData() {
      const res = fetch(`${API_BASE_URL}/transactions/1`)
        .then((res) => res.json())
        .then((parsed) => {
          this.data = parsed.data;
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
});
