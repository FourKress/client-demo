export default [
  {
    name: '首页',
    id: 'index',
    icon: 'ustax',
    children: [
      {
        path: '/',
        name: '发票管理',
        id: 'InvoiceList',
        icon: 'icon-invoice',
      },
    ],
  },
  {
    name: '打印列表',
    id: 'index',
    icon: 'print',
    children: [
      {
        path: '/printing',
        name: '正在打印',
        id: 'PrintingList',
        icon: 'icon-printing',
      },
      {
        path: '/printed',
        name: '打印完成',
        id: 'PrintedList',
        icon: 'icon-printed',
      },
    ],
  },
  {
    name: '下载列表',
    id: 'index',
    icon: 'download',
    children: [
      {
        path: '/DownloadingList',
        name: '正在下载',
        id: 'DownloadingList',
        icon: 'icon-downloading',
      },
      {
        path: '/DownloadedList',
        name: '下载完成',
        id: 'DownloadedList',
        icon: 'icon-downloaded',
      },
    ],
  },
];
