<template>
  <div class="w-full max-w-md px-2 py-16 sm:px-0">
    <TabGroup>
      <TabList class="flex space-x-1 rounded-xl bg-blue-900/20 p-1">
        <Tab
          v-for="name in names"
          as="template"
          :key="name"
          v-slot="{ selected }"
        >
          <button @click="changeSelected(name)"
            :class="[
              'w-full rounded-lg py-2.5 text-sm font-medium leading-5 text-blue-700',
              'ring-white ring-opacity-60 ring-offset-2 ring-offset-blue-400 focus:outline-none focus:ring-2',
              selected
                ? 'bg-white shadow'
                : 'text-blue-100 hover:bg-white/[0.12] hover:text-white',
            ]"
          >
            {{ name }}
          </button>
        </Tab>
      </TabList>
    </TabGroup>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { TabGroup, TabList, Tab } from '@headlessui/vue'
const emit = defineEmits(['name-selected'])

function changeSelected(name){
    emit('name-selected', name)
}
const names = ref(["Jan", "Felix", "Wieland"])
</script>
