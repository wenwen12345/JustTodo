<script setup lang="ts">
import Task from './components/Task.vue'
import { NMessageProvider } from 'naive-ui'
</script>

<template>
        <n-message-provider>
            <Task />
        </n-message-provider>
</template>