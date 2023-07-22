<template>
  <div>
    <label for="price" class="block text-sm font-medium leading-6 text-gray-900">Price</label>
    <div class="relative mt-2 rounded-md shadow-sm">
      <div class="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3">
        <span class="text-gray-500 sm:text-sm">€</span>
      </div>
      <input @input="priceChanged($event.target.value)" type="text" name="price" id="price" class="block w-full rounded-md border-0 py-1.5 pl-7 pr-20 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="0.00" />
      <div class="absolute inset-y-0 right-0 flex items-center">
        <label for="currency" class="sr-only">Currency</label>
      </div>
    </div>
  </div>
</template>

<script setup>
import {ref} from 'vue'

const emit = defineEmits(['price-changed'])

function priceChanged(price) {
    emit('price-changed', price)
}
</script>
