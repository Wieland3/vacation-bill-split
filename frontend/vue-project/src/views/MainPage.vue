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
      <div>
        <p class="mt-8 text-2xl">Total amount: {{totalAmount}} €</p>
      </div>
      <div> Test for continues deployment </div>
  </div>
</template>

<script setup>
import UserSelect from "@/components/UserSelect.vue";
import PriceInput from "@/components/PriceInput.vue";
import {onMounted, ref} from 'vue';
import axios from 'axios'

let currentPrice = ref('')
let currentName = ref('Jan')
let totalAmount = ref('0')


onMounted(async () => {
    await fetchAmount()
})

async function fetchAmount() {
    try {
        const response = await axios.get('/get-cash')
        totalAmount.value = response.data['amount']
    } catch (error) {
        console.error(error)
    }
}

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
        await fetchAmount();
    } catch (error) {
        console.error(error)
    }
}
</script>