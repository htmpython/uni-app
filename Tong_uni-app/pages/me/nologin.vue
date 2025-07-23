<template>
	<!-- 未登录页面 -->
	<view class="nologin-box">
		<image class="login-img" src="../../static/me/nologin.svg" mode="widthFix"></image>

		<view class="title">置若罔闻</view>
		<view class="description">一直敲一扇不开的门，是不礼貌的</view>
		<button class="login-btn" @tap="login">登录</button>
		<view class="bottom-box">
			<view class="no-login" @tap="toIndex">暂不登录</view>
			<view class="privacy" @tap="toPrivacy">隐私协议</view>
		</view>
	</view>

</template>

<script>
	export default {
		data() {
			return {

			}
		},
		onLoad() {

		},
		methods: {
			// 点击暂不登录
			toIndex() {
				uni.reLaunch({
					url: "/pages/index/index"
				})
			},
			// 点击隐私协议
			toPrivacy() {
				uni.navigateTo({
					url: "/pages/me/parvacy"
				})
			},
			// 点击登录
			async login() {
				// 弹窗获取权限
				const show_res = await uni.showModal({
					title: '提示',
					content: '请您仔细阅读《隐私协议》，点击确认即代表您已阅读并同意'
				})
				if (show_res.cancel === true) return;

				// 获取微信code
				const wx_res = await uni.login({
					provider: "weixin"
				})
				console.log('微信：',wx_res);
				// 获取code失败时的弹窗
				if (!wx_res.code) return this.$public.showerror('登录失败，请重试!')
				// 将code发送到后端，以获取用户信息和token
				const login_res = await this.$request.post('/api/user', {
					code: wx_res.code
				})

				// 如果发送异常
				if (login_res.data.code !== 0) return this.$public.showerror('网络错误，请重试!')
				// 存储token和用户信息到本地
				uni.setStorageSync("token", login_res.data.token)
				uni.setStorageSync('user_info', login_res.data.user_info)

				// 返回我的页面
				const page = getCurrentPages();  
				const prevPage = page[page.length -2]
				uni.navigateBack(
				{
					success:()=> prevPage.$vm.reload()
				})

			},

		}
	};
</script>

<style lang="scss" scoped>
	.nologin-box {
		width: 76%;
		position: absolute;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);

		.login-img {
			width: 100%;
			border-radius: 20rpx;
			position: relative;
			overflow: hidden;
			height: 600rpx;
			margin-bottom: 30rpx;
		}

		.title {
			font-size: 38rpx;
			position: relative;
			margin: 30rpx 0;

		}

		.title::after {
			content: '';
			position: absolute;
			bottom: -16rpx;
			left: 0rpx;
			width: 96rpx;
			height: 8rpx;
			border-radius: 200rpx;
			background: linear-gradient(90deg, rgba(55, 110, 234, 1) 0%, rgba(255, 255, 255, 1) 100%);
		}

		.description {
			color: #807C7C;
			font-size: 26rpx;
			margin-top: 18rpx;
		}

		.login-btn {
			height: 80rpx;
			width: 550rpx;
			line-height: 80rpx;
			color: #FFFFFF;
			background-color: #007AFF;
			margin-top: 80rpx;
			padding: 0rpx 30rpx;
			border-radius: 100rpx;
		}

		.bottom-box {
			margin-top: 30rpx;
			display: flex;
			align-items: center;
			justify-content: center;

			.no-login {
				font-size: 26rpx;
				margin: 0 30rpx;
				color: #807c7c;
			}

			.privacy {
				color: #007AFF;
				font-size: 28rpx;
				margin: 0 30rpx;
			}
		}


	}
</style>