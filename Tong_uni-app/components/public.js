export default {
	// 校验登录状态
	loginState() {
		const token = uni.getStorageSync("token")
		return token && token.length !== 0;
	},
	showerror(content) {
		uni.showToast({
			icon: "error",
			title: content
		})
	},
	updateStorage(key, field, value) {
	  let data = uni.getStorageSync(key);
	  if (data && typeof data === 'object') {
	    data[field] = value;
	    uni.setStorageSync(key, data); // 覆盖写入整个对象
	  } else {
	    console.warn(`缓存 "${key}" 不存在或不是一个对象`);
	  }
	}
}