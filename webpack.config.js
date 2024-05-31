const path = require("path");
const { CleanWebpackPlugin } = require("clean-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const CopyWebpackPlugin = require("copy-webpack-plugin");

module.exports = {
  mode: "development",
  entry: {
    bundle: "./src/index.js",
  },
  output: {
    path: path.resolve(__dirname, "static"),
    filename: "assets/js/[name].js",
    clean: true,
  },
  devtool: "source-map",
  module: {
    rules: [
      {
        test: /\.scss$/,
        use: [
          MiniCssExtractPlugin.loader,
          "css-loader",
          "postcss-loader",
          "sass-loader",
        ],
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
          options: {
            presets: ["@babel/preset-env"],
          },
        },
      },
      {
        test: /\.(png|svg|jpg|jpeg|gif)$/i,
        type: "asset/resource",
        generator: {
          filename: "assets/images/[name][ext]",
        },
      },
    ],
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: "assets/css/style.css",
    }),
    new CleanWebpackPlugin(),
    new CopyWebpackPlugin({
      patterns: [
        {
          from: "src/images",
          to: "assets/images",
          globOptions: {
            ignore: ["**/*.!(png|svg|jpg|jpeg|gif|webp)"],
          },
          noErrorOnMissing: true,
        },
        {
          from: "src/icons",
          to: "assets/icons",
          globOptions: {
            ignore: ["**/*.!(png|svg|jpg|jpeg|gif|webp)"],
          },
          noErrorOnMissing: true,
        },
      ],
    }),
  ],
};
