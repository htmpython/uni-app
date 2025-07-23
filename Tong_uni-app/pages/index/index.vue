<template>
	<view>
		<!-- 顶部背景 -->
		<image style="width: 100%;" src="../../static/index/top_img.svg" mode="aspectFill"></image>
		<!-- 轮播图 -->
		<view class="swiper-box">
			<u-swiper :list="carousel_list" height="320rpx" keyName="poster_url" showTitle circular duration=800
				imgMode="scaleToFill" radius="16rpx"></u-swiper>
		</view>
		<!-- 金刚区 -->
		<view class="vajra-box">
			<u-grid :border="false" @click="click" col="4">
				<u-grid-item v-for="(item,index) in vajar_list" :key="index" @click="vajarTo(item.target_url)">
					<image :src="item.icon_url" mode="aspectFill"></image>
					<text class="grid-text">{{item.text}}</text>
				</u-grid-item>
			</u-grid>
			<u-toast ref="uToast" />
		</view>
		<view class="tabs-box">
			<!-- 左侧区域 -->
			<view class="left">
				<image src="../../static/index/index_hot.svg" mode=""></image>
				<u-tabs :list="tabs_list" @click="selectTab()" :activeStyle="{color: '#dd0a3b'}" 
				:inactiveStyle="{color: '#7f7f7f',}">
				</u-tabs>
			</view>
			<!-- 右侧区域 -->
			<view class="right" @click="getCarouse()">
				<text>查看更多</text>
			</view>
		</view>
		<!-- 动态内容展示 -->
		<tong-post-list :post_list="post_list"></tong-post-list>
		

	</view>
</template>

<script>
	export default {
		data() {
			return {
				carousel_list: [],

				vajar_list: [],

				tabs_list: [{
					name: '最热'
				}, {
					name: '最新'
				}],

				post_list: [{
					img_url: '../../static/index/本人.jpg',
					avatar_url: '../../static/index/本人.jpg',
					user_name: '枫Sir',
					content: 'Thomas Juul Krahn 宇宙中最孤独的人宇宙中最孤独的人宇宙中最孤独的人宇宙中最孤独的人宇宙中最孤独的人宇宙中最孤独的人宇宙中最孤独的人宇宙中最孤独的人宇宙中最孤独的人宇宙中最孤独的人宇宙中最孤独的人宇宙中最孤独的人- -'
				},{
					img_url: '../../static/index/本人.jpg',
					avatar_url: '../../static/index/本人.jpg',
					user_name: '枫Sir',
					content: 'Thomas Juul Krahn 宇宙中最孤独的人宇宙中最孤独的人宇宙中最孤独的人宇宙中最孤独的人宇宙中最孤独的人宇宙中最孤独的人宇宙中最孤独的人宇宙中最孤独的人宇宙中最孤独的人宇宙中最孤独的人宇宙中最孤独的人宇宙中最孤独的人- -'
				},]


			}
		},
		onLoad() {
			this.getCarouse()
			this.getVajra()
		},
		methods: {
			
			// 获取轮播图数据
			getCarouse() {
			    this.$request.get('/api/carousels').then(res => {
			        this.carousel_list = res.data
					console.log(this.carousel_list);
			    })
			},
			
			getVajra(){
				this.$request.get('/api/vajras').then(res=>{
					this.vajar_list = res.data
					console.log(this.vajar_list);
				})
			},
			
			// 金刚区点击
			vajarTo(item) {
				uni.navigateTo({
					url: item,
				})
			},
			// 最新tabs切换
			selectTab(item) {
				console.log(item);

			},
			
			

		}
	}
</script>

<style lang="scss">
	// 金刚区样式
	.vajra-box {
		background-color: #ffffff;
		padding: 14rpx;
		margin: 20rpx;
		border-radius: 16rpx;

		image {
			height: 80rpx;
			width: 80rpx;
		}

		text {
			padding: 8rpx 0;
			font-size: 24rpx;
			color: #807c7c;
		}
	}

	// 最新最热tabs样式
	.tabs-box {
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin: 0 32rpx;

		.left {
			display: flex;
			justify-content: flex-start;
			align-items: center;

			image {

				height: 42rpx;
				width: 42rpx;
			}
		}

		.right {
			color: #989898;
			height: 80rpx;
			line-height: 80rpx;
			font-size: 28rpx;
		}

	}

	// 轮播图样式
	.swiper-box {
		margin: -200rpx 30rpx 30rpx 30rpx;
		/* 解决轮播图圆角闪动问题 */
		will-change: transform;
	}

	

	@media (prefers-color-scheme: dark) {
		// 金刚区样式
		.vajra-box {
			background: #323232;

			text {
				color: #e1e1e1;
			}
		}




	}
</style>