// src/stores/types.js
import { defineStore } from "pinia";

const API_BASE_URL = "http://localhost:5000/api";

export const useTypesStore = defineStore("types", {
  state: () => ({
    data: null,
  }),
  actions: {
    async fetchData() {
      const res = await fetch(`${API_BASE_URL}/types/1`);
      const parsed = await res.json();
      this.data = parsed.data;
    },
  },
});
