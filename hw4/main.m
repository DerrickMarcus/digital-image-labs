% homework 4: log transformation

load('./work.mat');

spectrum = abs(image);
c = 1;
log_spectrum = c * log(1 + spectrum);

figure;
subplot(1, 2, 1);
imagesc(spectrum);
title('Original specturm');
xlabel('X');
ylabel('Y');
colormap(gray); % 使用灰度映射
colorbar; % 添加颜色条

subplot(1, 2, 2);
imagesc(log_spectrum);
title('Spectrum after log transformation');
xlabel('X');
ylabel('Y');
colormap(gray);
colorbar;

saveas(gcf, 'result.jpg');
