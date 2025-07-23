<template>
	<view>
		<view class="que-user-view">
			<span class="que-user-red">*</span>注意 : 用户昵称中不得带有明显低俗或侮辱性词汇组合，不得违反《网络信息内容生态治理规定》第六条、第七条规定
		</view>
		<button class="avatar-wrapper" open-type="chooseAvatar" @chooseavatar="updateAvatar">
			<image class="avatar" :src="avatarUrl" mode=""></image>
			<image class="picture" src="../../static/me/picture.svg" mode=""></image>
		</button>
		<!-- 输入框 -->
		<view class="name-view">
			<image class="name-icon" src="../../static/me/username.svg" mode=""></image>
			<!-- nickname -->
			<input type="nickname" @input="bindinputN" class="name-input" placeholder="输入昵称" :value="inputValue" />
		</view>

		<view class="name-view">
			<image class="name-icon" src="../../static/me/userdsrc.svg" mode=""></image>
			<input class="name-input" @input="bindinputC" placeholder="输入个性签名" :value="onKeyDesrc" />
		</view>

		<u-toast ref="uToast"></u-toast>

		<button class="name-btn" @tap="keyInfo()">保存</button>
	</view>
</template>

<script>
	import avatar from '../../uni_modules/uview-ui/libs/config/props/avatar'
	export default {
		data() {
			return {
				avatarUrl: '../../static/me/user.png',
				inputValue: '',
				onKeyDesrc: '',
				user: []
			}
		},
		onLoad() {
			this.getUserInfo()
		},
		methods: {
			// 获取用户信息
			getUserInfo() {
				const user_info = uni.getStorageSync("user_info")
				if (user_info) {
					this.avatarUrl = user_info.avatar_url
					this.inputValue = user_info.name
					this.onKeyDesrc = user_info.introduction
				}
			},
			// 传头像
			async updateAvatar(e) {
				uni.uploadFile({
					url: "http://127.0.0.1:8000/api/update",
					filePath: e.detail.avatarUrl,
					name: "avatar",
					header: {
						'Authorization': uni.getStorageSync("token")
					},
					success: (res) => {
						// 手动解析json字符串
						if (typeof res.data === 'string') {
							try {
								res.data = JSON.parse(res.data)
							} catch (e) {
								console.error('解析失败');
								return
							}
						}
						// 同步更换头像
						this.avatarUrl = res.data.avatar_url
						// 更新缓存
						this.$public.updateStorage("user_info", "avatar_url", res.data.avatar_url)
					}

				})
			},
			// 获取昵称
			bindinputN(event) {
				this.inputValue = event.detail.value
			},
			bindinputC(event) {
				this.onKeyDesrc = event.detail.value
			},

			async keyInfo() {
				if (this.inputValue === '') {
					this.$refs.uToast.show({
						message: '昵称不能为空',
						type: 'error'
					});
					return;
				};

				let userinfo_key = {
					avatar_url: this.avatarUrl,
					name: this.inputValue,
					introduction: this.onKeyDesrc
				}

				this.$request.put("/api/update", userinfo_key)
				.then((res) => {
					// 更新缓存
					uni.setStorageSync("user_info", userinfo_key)

					let page = getCurrentPages();
					let prevPage = page[page.length - 2]
					if (typeof(prevPage) == "undefined") return;
					prevPage.$vm.reload();
					
					this.$refs.uToast.show({
						message: '信息修改成功！',
						type: 'success',
						complete() {
							uni.navigateBack()
						}
					})

				}).catch(err => {
					this.$refs.uToast.show({
						message: '保存失败，请稍后再试',
						type: 'error'
					});
					console.error('请求失败:', err);
				});



			}
		}

	}
</script>

<style lang="scss">
	/* 保存按钮 */
	.name-btn {
		background-color: #007aff;
		border-radius: 100rpx;
		height: 90rpx;
		width: 450rpx;
		line-height: 90rpx;
		color: #ffffff;
		margin-top: 100rpx;
	}

	.que-user-view {
		background-color: #f7f7f7;
		margin: 40rpx;
		padding: 30rpx;
		color: #888888;
		font-size: 26rpx;
		border-radius: 20rpx;

		.que-user-red {
			color: #cc0000;
			margin-right: 8rpx;
			font-size: 32rpx
		}
	}




	/* 头像点击按钮 */
	.avatar-wrapper {
		background-color: #f7f7f7;
		padding: 0;
		width: 140rpx !important;
		height: 180rpx;
		border-radius: 16rpx;
		margin-top: 40rpx;
		margin-bottom: 40rpx;
		position: relative;

		.avatar {
			display: block;
			width: 140rpx;
			height: 140rpx;
		}

		.picture {
			width: 60rpx;
			height: 60rpx;
			position: absolute;
			top: 130rpx;
			left: 40rpx;
		}

	}

	.avatar-wrapper::after {
		border: none;
		/* uni-app 默认按钮有伪类边框，需要额外去掉 */
	}

	.name-view {
		position: relative;
		width: 100%;
		margin-bottom: 36rpx;
		left: 8.8%;

		/* icon图标*/
		.name-icon {
			position: absolute;
			left: 20rpx;
			top: 50%;
			transform: translateY(-50%);
			height: 55rpx;
			width: 55rpx;
			pointer-events: none;
			/* 防止图片阻挡输入框点击 */
		}

		/* 输入框 */
		.name-input {
			padding-left: 98rpx;
			/* 要比图标的宽度稍大一些，防止文字重叠 */
			font-size: 32rpx;
			width: 70%;
			height: 120rpx;
			background-color: #f7f7f7;
			border-radius: 16rpx;

		}

	}






	@media (prefers-color-scheme: dark) {
		.avatar-wrapper {
			background-color: #191919;
		}

		.name-view {
			.name-input {
				background-color: #232323;
			}
		}

		.que-user-view {
			background-color: #232323;
		}
	}
</style>