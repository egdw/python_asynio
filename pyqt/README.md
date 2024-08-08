# PyQT的异步操作

## 一种是基于QTimer

自己定义周期，不能直接用time.sleep()，否则也会被延时

## 一种是基于QThread

要自己定义槽，然后去连接槽