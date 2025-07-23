const request = (url, method = 'GET', data = {}, contentType = 'application/json') => {
	return new Promise((resolve, reject) => {
		uni.request({
			url: "http://192.168.5.1:8000" + url,
			data: data,
			method: method,
			header: {
				contentType: contentType,
				// 请求时携带token信息
				'Authorization': uni.getStorageSync("token")
			},
			success(res) {
				resolve(res)
			},
			fail(err) {
				uni.showToast({
					title: '系统异常',
					icon: 'fail',
					duration: 2000
				})
			}
		})
	})
}

// 定义对象属性并抛出，属性的值为request函数
export default {
	get: (url, data) => request(url, 'GET', data),
	post: (url, data) => request(url, 'POST', data),
	delete: (url, data) => request(url, 'DELETE', data, 'application/x-www-form-urlencoded'),
	put: (url, data) => request(url, 'PUT', data),
}