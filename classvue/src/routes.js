import {createWebHistory, createRouter} from 'vue-router'
import HomePage from './components/Home.vue';
import LoginC2 from './components/Login2.vue';
import AddStudent from "@/components/AddStudent.vue";
import ReceiptM from "@/components/Receipt.vue";
import ShowReceipts from "@/components/ShowReceipts.vue";

const routes = [
    {
        name:'Login2',
        path:'/',
        component:LoginC2
    },
    {
        name:'Home',
        path:'/home',
        component:HomePage
    },
    {
        name:'AddStudent',
        path:'/addstu',
        component:AddStudent
    },
    {
        name:'Receipt',
        path:'/receipt/:id',
        component:ReceiptM
    },
    {
        name:'ShowReceipts',
        path:'/showreceipts/:id',
        component:ShowReceipts
    },
]

const router=createRouter({
    history:createWebHistory(),
    routes
})

export default router;