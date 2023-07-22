<template>
  <div class="flex flex-col items-center">
    <UserSelect @name-selected="handleNameSelected" />
      <div class="flex">
        <PriceInput @price-changed="handlePriceChanged"/>
          <div>
            <button @click="sendMoney" class="mt-8 bg-blue-500 hover:bg-blue-700 text-white px-6 py-2 rounded-xl text-sm">
             Submit
            </button>
          </div>
      </div>
  </div>
</template>

<script setup>
import UserSelect from "@/components/UserSelect.vue";
import PriceInput from "@/components/PriceInput.vue";
import { ref } from 'vue';
import axios from 'axios'

let currentPrice = ref('')
let currentName = ref('Jan')

function handleNameSelected(name) {
  currentName.value = name
}
function handlePriceChanged(price) {
    currentPrice.value = price
}

async function sendMoney() {
    const data = {name: currentName.value, price: currentPrice.value}

    try {
        const response = await axios.post('/send-cash', data)
    } catch (error) {
        console.error(error)
    }
}
</script>